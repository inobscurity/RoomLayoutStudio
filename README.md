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
3. After a minute the app is at `https://inobscurity.github.io/RoomLayoutStudio/`. The address is case-sensitive: keep the capitals. Open that on your
   phone. In Safari or Chrome you can choose **Add to Home Screen** to get an app icon.

On a computer you can also download `index.html` and open it in a browser.

**New to it?** Press **How it works** (on the example room, or under Project) for a seven-step walkthrough.

## How measuring from a photo works

One photo only gives you sizes if something of known size lies flat in it. Room Layout Studio uses a reference
rectangle: a sheet of A4 or Letter paper, a bank card, a floor tile, or anything you've measured, such as a
rug. You tap its four corners, and the app works out the perspective of that flat surface (a planar
homography). Any two points you tap on the same surface can then be measured in centimetres or inches.

- **Upright step (room photos).** A sheet of paper is big enough to set the scale, but too small to show how
  the camera was tilted. After you mark the paper, the app finds upright edges in the photo, such as door
  frames, cupboard sides and wall corners, and uses them for the tilt. It reads the lens's focal length from
  the photo (phones record it). It then shows the **camera height**, which should be about where you held
  the phone. That's a quick check the photo is set up right. You can remove or add edges by tapping. If the
  photo has no lens information (screenshots, photos sent through some chat apps), type the 35 mm-equivalent
  focal length; most phone main cameras are 23–26 mm.
- **Room photo (the floor).** Tap the corners where the walls meet the floor to get the wall lengths and the
  room shape. Three corners are enough for a rectangular room. Then tap where each piece of furniture
  touches the floor (front-left, front-right, one back corner). That gives its width and depth, and it is
  placed on the plan where it actually stands.
- **Furniture photo (the front).** Hold or tape a sheet of paper flat against the front of the piece and
  photograph it straight on. Tap two points for the width and two for the height. Add the depth from a side
  photo or type it in.
- **Floor corners hidden by furniture?** Switch to **Ceiling corners**, both when tracing the room and when
  linking a photo, and tap where the walls meet the ceiling. A ceiling corner is straight above its floor
  corner, so the app uses the ceiling height from the Room tab to place it. Ceiling corners are less accurate
  than floor corners. The ceiling is close above the camera, so small errors grow, and in a real test a 4.96 m
  wall came out at 4.53 m. Use floor corners where you can, and correct the plan with one tape measurement. The Preview draws the whole room as a wireframe (floor, corners and ceiling), so you can check it
  lines up with the photo.
- **Things whose base is hidden,** like a bookcase or floor lamp behind a sofa. In the Furniture tool,
  choose **Top corners**, type the piece's height, and tap its top corners instead of its feet. Or choose
  **Top centre** and tap the top of a lamp. The app works out where the base is from the camera estimate.
  Measure the height with a tape, from a furniture photo, or with the **Height** tool: tap a point where a
  piece meets the floor, then the point straight above it.
- **Distance tool.** Measures between any two points on the floor.
- **The paper hasn't moved?** If the paper is in the same spot as in a photo you've already linked, choose
  **Same as photo N** under **Link to plan**. No corners are needed. The app works out which way round the
  paper was tapped, using where the window is bright in the photo, or where the camera must have stood. If
  the blue outline doesn't sit on the room, press **Turn it round**.
- **More room photos, from other angles** (as many as you like). Photograph the room from another corner, with the paper anywhere
  on the floor. Use **Link to plan** to tap two room corners you can see, matching each to a corner on a
  small plan of the room. After that, furniture you mark in that photo lands where it stands. You can also
  trace the room outline from it, for example the open-plan edge that only that angle shows.
- **Preview.** In a linked photo, Preview draws the current layout into the photo from where it was taken.
  Pieces with a height appear as see-through boxes. The app estimates the camera from the floor reference,
  so it's an approximation: boxes can lean or drift a little, most near the edges of the picture. **Layouts
  → See it in your photos** opens each linked photo, so you can view a layout from every angle you
  photographed.

- **3D view** (**3D view** below the plan, or **Layouts → See it in 3D**). It builds the room from the plan
  from your linked photos.
  - **Walls, floor and ceiling:** walls are drawn in their real paint colour, with each window cut from the
    photos where the plan puts it. The floor is a clean, evenly lit sample of your real boards, tiled with
    the boards running the right way. The ceiling is plain.
  - **Modelled furniture** (the default): each piece is built from simple parts at its exact measurements.
    A sofa gets a base, cushions and arms, a bookcase gets shelves and rows of books coloured from your
    photo, and a lamp gets a tripod and shade. Each is coloured from your photos, ignoring colours that
    can't belong to that kind of piece. The shape is worked out from the name, or chosen in the piece's
    settings (**Shape in the 3D view**).
  - **Photo blocks** (the other option): each piece is a block wearing its own pictures, front, sides and top, cut from the photo
    that shows each side best. Parts of a block that show the room behind the piece, not the piece itself,
    are cut away, so pieces keep roughly their real outline. Sides no photo shows are drawn flat in the
    piece's own colour.
  - **Viewpoints:** turn around the room, look from exactly where any photo was taken (to compare a new
    layout with the photo), or sit in any seat facing the TV.
  - **Options:** pick any layout, turn furniture off to see the bare room, and **Save image**.
  - **What it is:** an approximation, not a 3D model. Pieces look printed on boxes from very different
    angles, and clutter the plan doesn't know about can show up on walls or floors. The 3D library
    (three.js) loads from the internet the first time.
- **Save this view** in a photo's Preview saves the photo with the layout drawn in, at full size.

The app pairs the reference's long and short sides with the right edges in the photo by itself. If the
labelled side is still wrong, press **Swap sides**.

Accuracy depends on the reference. A bigger one is better, and points far from it are less accurate. Expect
a few percent of error with a sheet of paper. Check any measurement that matters with a tape.

## The floor plan

- Drag furniture to move it. Use the round handle to rotate it, which snaps to 15° steps. Press Rotate 90°
  for quarter turns. Furniture snaps flush to walls; you can turn snapping off in the Room tab.
- When a piece is selected, yellow lines show its distance to the nearest wall on each side. You can also
  show the distance to the nearest furniture.
- Furniture that overlaps another piece or goes through a wall is outlined in red. Rugs can be marked as
  lying on the floor so other furniture can stand on them.
- **Typed gaps:** the gaps to the walls in the panel can be typed in. Enter a distance you measured with a
  tape and the piece moves exactly there. This is handy for pieces you couldn't measure in a photo.
- **Openings:** **Room → Add opening** marks a gap in a wall with no door, such as a stairwell or an
  archway, with its width and height. It shows on the plan and in the 3D view.
- **Windows** have a sill height and a window height (Room tab, select the window). Furniture within 60 cm
  of a window, and taller than its sill, is flagged. That shows whether a TV on its cabinet would cover the
  window. Windows and doors are also drawn in the photo Preview.
- **Wall lengths:** type any wall's length in **Room → Walls**, in any room shape. The wall grows from its
  first corner, and the walls beyond it move to match (in a rectangle, the opposite wall).
- **Open-plan spaces:** in the Room tab, mark any side of the room as **Open** where there's no wall, and
  add corners with **Edit corners** to mark where the room's area ends. Open sides are drawn dashed.
  Furniture doesn't snap to them, wall distances ignore them, and furniture can cross them without a
  warning. It's only flagged once it is outside the room area.
- **Things on top of furniture:** set **Stands on** to put a piece on another one, such as a TV on a TV
  cabinet or a lamp on a side table. It moves and turns with the piece underneath in every layout. The app
  shows how high its top is, and warns if it sticks out past the edge. Drag it off to put it back on the
  floor. **Common sizes → TV stand with a TV on it** adds both at once, and **Put a TV on top** adds a TV
  sized to fit a cabinet.
- **TV viewing distance:** mark a piece as a TV and give its screen size. A dashed line runs from the
  screen to the seat most directly in front of it, showing the distance and whether it suits the screen.
  The rule of thumb is 1 to 1.6 times the screen diagonal for an immersive picture, and up to 2.5 times for
  comfortable viewing. Seats more than 30° to the side are flagged. Sofas, chairs and beds count as seats
  automatically, and any piece can be marked as one.
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
