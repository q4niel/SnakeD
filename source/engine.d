import std.stdio;
import third.glue.raylib.raylib;
import data;
import ientity;
import food;
import snake;

struct Engine {
    static IEntity[2] entities = [
        new Food(),
        new Snake()
    ];

    static Food getFood() => cast(Food)entities[0];
    static Snake getSnake() => cast(Snake)entities[1];

    static float prevDeltaTime = 0;
    static float deltaTime = 0;
    static float timeScale = .2;
    static float fixedTimer = 0;

    static Vector2 randomCell() => Vector2 (
        GetRandomValue(0, Data.cellCount - 1),
        GetRandomValue(0, Data.cellCount - 1)
    );

    static bool initialize() {
        InitWindow(Data.cellSize * Data.cellCount, Data.cellSize * Data.cellCount, Data.windowName.ptr);
        SetTargetFPS(Data.targetFPS);

        foreach (entity; entities) {
            entity.onInitialize();
        }

        return true;
    }

    static bool shouldProcess = true;
    static bool process() {
        shouldProcess = !WindowShouldClose();
        BeginDrawing();
        ClearBackground(Data.lightGreen);

        float time = GetTime();
        deltaTime = time - prevDeltaTime;
        prevDeltaTime = time;

        fixedTimer += deltaTime;
        while (fixedTimer >= timeScale) {
            foreach (entity; entities) {
                entity.onFixedProcess();
            }
            fixedTimer -= timeScale;
        }

        foreach (entity; entities) {
            entity.onProcess();
        }

        EndDrawing();
        return true;
    }

    static bool terminate() {
        foreach (entity; entities) {
            entity.onTerminate();
        }

        CloseWindow();
        return true;
    }
}