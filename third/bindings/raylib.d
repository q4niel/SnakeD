extern(C) {
    void InitWindow(int width, int height, const char *title);
    void CloseWindow();
    bool WindowShouldClose();
    void BeginDrawing();                                    // Setup canvas (framebuffer) to start drawing
    void EndDrawing();
    void SetTargetFPS(int fps);
}