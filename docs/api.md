# Python API

## `Background`

```{eval-rst}
.. autoclass:: getwinbg.Background
   :members:
   :undoc-members:
```

Create a `Background` instance, then read the current path through its
`path` property:

```python
from getwinbg import Background

background = Background()
path = background.path
```

### Reveal or open the file

`reveal()` asks File Explorer to select the background file:

```python
background.reveal()
```

`open()` launches the file with its default Windows application:

```python
background.open()
```

Both operations retrieve and validate the current path before acting on it.

## Deprecated compatibility API

The package also exports `get_background()`, which returns the current
background path as a string:

```python
from getwinbg import get_background

path = get_background()
```

`get_background()` is deprecated and will be removed in version 0.2.0. Use
`Background().path` instead.
