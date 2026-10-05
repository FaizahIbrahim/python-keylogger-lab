# pynput Keyboard Key Reference

This document contains notes on special keyboard keys recognised by
`pynput.keyboard.Key`.

## Modifier Keys

| Key | Description |
|---|---|
| `Key.alt` | Generic Alt key |
| `Key.alt_l` | Left Alt key |
| `Key.alt_r` | Right Alt key |
| `Key.ctrl` | Generic Ctrl key |
| `Key.ctrl_l` | Left Ctrl key |
| `Key.ctrl_r` | Right Ctrl key |
| `Key.shift` | Generic Shift key |
| `Key.shift_l` | Left Shift key |
| `Key.shift_r` | Right Shift key |
| `Key.cmd` | Windows/Super key on Windows or Command key on macOS |

## Editing and Navigation Keys

| Key | Description |
|---|---|
| `Key.backspace` | Backspace |
| `Key.delete` | Delete |
| `Key.enter` | Enter / Return |
| `Key.space` | Space |
| `Key.tab` | Tab |
| `Key.home` | Home |
| `Key.end` | End |
| `Key.page_up` | Page Up |
| `Key.page_down` | Page Down |
| `Key.left` | Left arrow |
| `Key.right` | Right arrow |
| `Key.up` | Up arrow |
| `Key.down` | Down arrow |
| `Key.esc` | Escape |

## Other Keys

- `Key.caps_lock`
- `Key.num_lock`
- `Key.scroll_lock`
- `Key.insert`
- `Key.print_screen`
- `Key.pause`
- `Key.menu`
- Function keys such as `Key.f1`, `Key.f2`, etc.

## Keys Used in This Project

The current keyboard listener specifically handles:

- `Key.space` → converted into a normal space
- `Key.enter` → converted into a new line
- `Key.shift_l` → ignored/replaced
- `Key.shift_r` → ignored/replaced
