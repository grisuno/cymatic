# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 2 | **Total Symbols Extracted:** 4 | **Total Imports:** 4

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    app_py["app.py (py)"]
    class app_py mod;
    app_py_CymaticsVisualizer["CymaticsVisualizer"]
    class app_py_CymaticsVisualizer cls;
    app_py --> app_py_CymaticsVisualizer
    app_py___init__["__init__"]
    class app_py___init__ fn;
    app_py --> app_py___init__
    app_py_draw_cymatic["draw_cymatic"]
    class app_py_draw_cymatic fn;
    app_py --> app_py_draw_cymatic
    app_py_visualize["visualize"]
    class app_py_visualize fn;
    app_py --> app_py_visualize
    install_sh["install.sh (sh)"]
    class install_sh mod;
    ext_tkinter["tkinter"]
    class ext_tkinter ext;
    app_py -.->|imports| ext_tkinter
    app_py -.->|imports| ext_tkinter
    ext_numpy["numpy"]
    class ext_numpy ext;
    app_py -.->|imports| ext_numpy
    ext_matplotlib_pyplot["matplotlib.pyplot"]
    class ext_matplotlib_pyplot ext;
    app_py -.->|imports| ext_matplotlib_pyplot
```

---

## Architecture Reference

### PY (1 files)

#### `app.py`
**Path:** `app.py`

**Classes:**
- `CymaticsVisualizer` (line 18) `class CymaticsVisualizer`

**Functions:**
- `__init__` (line 19) `def __init__(self, root)`
- `draw_cymatic` (line 40) `def draw_cymatic(self, frequency)`
- `visualize` (line 67) `def visualize(self)`

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
