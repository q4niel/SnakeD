import third.glue.raylib.raylib;
import data;

bool init() {
    InitWindow(cellSize * cellCount, cellSize * cellCount, windowName.ptr);
    SetTargetFPS(targetFPS);

    return true;
}

bool runProc = true;
bool proc() {
    runProc = !WindowShouldClose();
    BeginDrawing();

    ClearBackground(lightGreen);

    EndDrawing();
    return true;
}

bool term() {
    CloseWindow();
    return true;
}