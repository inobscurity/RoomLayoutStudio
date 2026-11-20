# Room Layout Studio

Room Layout Studio is a room layout planner that runs in the browser. You photograph a room and its furniture, and it
measures the walls and the furniture from the photos. You then drag the furniture around a scale floor plan
to try different layouts. It's a single file, `index.html`, and needs no install or server. Open it on a
phone or a computer.

## Use it on your phone

The easiest way is to publish it with GitHub Pages, which is free:

1. On GitHub, open this repository's **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to *Deploy from a branch*, choose branch `main` and
   folder `/ (root)`, then press **Save**.
3. After a minute the app is at `https://inobscurity.github.io/roomlayoutstudio/`. Open that on your
   phone. In Safari or Chrome you can choose **Add to Home Screen** to get an app icon.

On a computer you can also download `index.html` and open it in a browser.

## How measuring from a photo works

One photo only gives you sizes if something of known size lies flat in it. Room Layout Studio uses a reference
rectangle: a sheet of A4 or Letter paper, a bank card, a floor tile, or anything you've measured, such as a
rug. You tap its four corners, and the app works out the perspective of that flat surface (a planar
homography). Any two points you tap on the same surface can then be measured in centimetres or inches.

- **Room photo (the floor).** Tap the corners where the walls meet the floor to get the wall lengths and the
  room shape. Three corners are enough for a rectangular room. Then tap where each piece of furniture
  touches the floor (front-left, front-right, one back corner). That gives its width and depth, and it is
  placed on the plan where it actually stands.
- **Furniture photo (the front).** Hold or tape a sheet of paper flat against the front of the piece and
  photograph it straight on. Tap two points for the width and two for the height. Add the depth from a side
  photo or type it in.
- **Distance tool.** Measures between any two points on the floor.

Accuracy depends on the reference. A bigger one is better, and points far from it are less accurate. Expect
a few percent of error with a sheet of paper. Check any measurement that matters with a tape.

## The floor plan

- Drag furniture to move it. Use the round handle to rotate it, which snaps to 15° steps. Press Rotate 90°
  for quarter turns. Furniture snaps flush to walls; you can turn snapping off in the Room tab.
- When a piece is selected, yellow lines show its distance to the nearest wall on each side. You can also
  show the distance to the nearest furniture.
- Furniture that overlaps another piece or goes through a wall is outlined in red. Rugs can be marked as
  lying on the floor so other furniture can stand on them.
- **Layouts:** keep several arrangements of the same room and furniture, and switch between them.
- **Room tab:** type the room size, drag the corners of an irregular room, and add doors (with their
  swing) and windows.
- **Save image:** a PNG of the current layout with the room size, a scale bar and a list of the furniture.
  On a phone it opens the share sheet so you can save it to Photos or send it.
- Metric or imperial units, undo and redo (Ctrl+Z, Ctrl+Shift+Z), and arrow keys to nudge the selected
  piece.

The project saves automatically in the browser (IndexedDB). **Project → Export file** saves a JSON copy,
photos included, that you can import on another device.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole app: HTML, CSS and JavaScript. |
| `build-artifact.sh` | Builds the copy published as a claude.ai Artifact: the same page without its `<html>`/`<head>` wrapper. |
