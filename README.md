Issue tracked at [Nuitka/XXX](https://github.com/Nuitka/Nuitka/issues/XXX)

Nuitka 0.6.5 fixed some issues when asyncio exceptions were triggered (see [Nuitka/165](https://github.com/Nuitka/Nuitka/issues/165) & [Nuitka/213](https://github.com/Nuitka/Nuitka/issues/213)). The compiled code no longer throw a `RuntimeError` exception however it looks like it is causing a memory leak. The number of objects reported by `gc.get_objects()` is always increasing (same for the RSS memory of the process).

In this reproducer, the URL `http://127.0.0.1` must not response to HTTP request so a `aiohttp.client_exceptions.ClientConnectorError` exception will be raised. When run with native Python, the number of object is not increasing at all but it is with the compiled code.

Tested with Nuitka 0.6.5 and Python 3.7.5.

### Running on Linux (Docker) with native Python 3.7.5

```
# ./run-native.sh
( ... docker building the image ... )

Objects before HTTP loop
builtins.function                       5692     +5692
builtins.dict                           3229     +3229
builtins.tuple                          3069     +3069
builtins.weakref                        1386     +1386
builtins.wrapper_descriptor             1280     +1280
builtins.builtin_function_or_method      988      +988
builtins.method_descriptor               969      +969
builtins.getset_descriptor               887      +887
builtins.list                            878      +878
builtins.type                            813      +813


Objects after HTTP loop

Objects Count Diff: 0
```

### Running on Linux (Docker), compiled with Nuitka 0.6.5 on Python 3.7.5

```
# ./run-nuitka.sh
( ... docker building the image ... )

Objects before HTTP loop
builtins.function                       4483     +4483
builtins.dict                           3171     +3171
builtins.tuple                          2737     +2737
builtins.weakref                        1494     +1494
builtins.compiled_function              1355     +1355
builtins.wrapper_descriptor             1287     +1287
builtins.builtin_function_or_method     1039     +1039
builtins.method_descriptor               987      +987
builtins.getset_descriptor               931      +931
builtins.list                            919      +919


Objects after HTTP loop
builtins.compiled_cell                   709      +460
builtins.list                           1079      +160
builtins.dict                           3321      +150
builtins.traceback                       132      +120
builtins.tuple                          2837      +100
builtins.compiled_frame                  592       +74
multidict._multidict_py.CIMultiDict       55       +50
multidict._multidict_py._Impl             55       +50
builtins.frame                            55       +50
builtins.set                             156       +30

Objects Count Diff: 1537
```
