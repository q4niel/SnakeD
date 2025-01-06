import ientity;
import third.glue.raylib.raylib;
import third.glue.raylib.raymath;
import data;
import engine;
import food;

class Snake : IEntity {
    Vector2[] body = [
        {6, 9},
        {5, 9},
        {4, 9}
    ];

    Vector2 dir = {1, 0};

    void onInitialize() {}

    void onProcess() {
        for (int i = 0; i < body.length; i++) {
            if (IsKeyPressed(KEY_UP)) dir = Vector2(0, -1);
            if (IsKeyPressed(KEY_DOWN)) dir = Vector2(0, 1);
            if (IsKeyPressed(KEY_LEFT)) dir = Vector2(-1, 0);
            if (IsKeyPressed(KEY_RIGHT)) dir = Vector2(1, 0);

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

        grow();
        body = body[0..$-1];

        Food food = Engine.getFood();
        if (Vector2Equals(body[0], food.pos)) {
            food.respawn();
            grow();
        }
    }

    void onTerminate() {}
}