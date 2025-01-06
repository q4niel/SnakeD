import third.glue.raylib.raylib;
import data;

struct Engine {
    static bool on() {
        InitWindow(Data.cellSize * Data.cellCount, Data.cellSize * Data.cellCount, Data.windowName.ptr);
        SetTargetFPS(Data.targetFPS);

        return true;
    }

    static bool runnable = true;
    static bool run() {
        runnable = !WindowShouldClose();
        BeginDrawing();

        ClearBackground(Data.lightGreen);

        EndDrawing();
        return true;
    }

    static bool off() {
        CloseWindow();
        return true;
    }
}