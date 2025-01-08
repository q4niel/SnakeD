import ientity;
import third.glue.raylib.raylib;
import third.glue.raylib.raymath;
import data;
import engine;
import food;
import std.stdio;

class Snake : IEntity {
    bool isMoving = false;

    Vector2[] body = [
        Vector2(),
        Vector2(),
        Vector2()
    ];

    Vector2 dir = Vector2();

    void onInitialize() {
        respawn();
    }

    void onProcess() {
        if (!isMoving) {
            if (
                IsKeyPressed(KEY_UP)
            ||  IsKeyPressed(KEY_DOWN)
            ||  IsKeyPressed(KEY_LEFT)
            ||  IsKeyPressed(KEY_RIGHT)
            ) {
                isMoving = true;
            }
        }

        if (IsKeyPressed(KEY_UP) && dir.y != 1) dir = Vector2(0, -1);
        if (IsKeyPressed(KEY_DOWN) && dir.y != -1) dir = Vector2(0, 1);
        if (IsKeyPressed(KEY_LEFT) && dir.x != 1) dir = Vector2(-1, 0);
        if (IsKeyPressed(KEY_RIGHT) && dir.x != -1) dir = Vector2(1, 0);

        for (int i = 0; i < body.length; i++) {
            DrawRectangleRounded (
                Rectangle (
                    cast(int) body[i].x * Data.cellSize,
                    cast(int) body[i].y * Data.cellSize,
                    Data.cellSize,
                    Data.cellSize
                ),
                .5,
                6,
                Data.darkGreen
            );
        }
    }

    void onFixedProcess() {
        void grow() {
            body = Vector2Add(body[0], dir) ~ body;
        }

        if (isMoving) {
            grow();
            body = body[0..$-1];
        }

        Food food = Engine.getFood();
        if (Vector2Equals(body[0], food.pos)) {
            food.respawn();
            grow();
        }

        if (
            body[0].x >= Data.cellCount
        ||  body[0].x <= -1
        ||  body[0].y >= Data.cellCount
        ||  body[0].y <= -1
        ) {
            respawn();
        }

        foreach (part; body[1..$]) {
            if (Vector2Equals(body[0], part)) {
                respawn();
            }
        }
    }

    void onTerminate() {}

    void respawn() {
        isMoving = false;

        body = [
            Vector2(6, 9),
            Vector2(5, 9),
            Vector2(4, 9)
        ];

        dir = Vector2(1, 0);

        Engine.getFood().respawn();
    }
}