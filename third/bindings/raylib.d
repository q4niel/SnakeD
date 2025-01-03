extern(C) {
    void InitWindow(int width, int height, const char *title);
    void CloseWindow();
    bool WindowShouldClose();
    void BeginDrawing();
    void EndDrawing();
    void SetTargetFPS(int fps);
}