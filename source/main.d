import std.stdio;
import third.glue.raylib;

int main(string[] args) {
    InitWindow(750, 750, "SnakeD");
    SetTargetFPS(60);

    while (!WindowShouldClose()) {
        BeginDrawing();
        EndDrawing();
    }

    CloseWindow();
    return 0;
}