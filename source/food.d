import ientity;
import third.glue.raylib.raylib;
import third.glue.raylib.raymath;
import engine;
import data;
import snake;

class Food : IEntity {
    Vector2 pos = {};

    void onInitialize() => respawn();

    void onProcess() {
        DrawRectangle (
            cast(int) pos.x * Data.cellSize,
            cast(int) pos.y * Data.cellSize,
            Data.cellSize,
            Data.cellSize,
            Data.darkGreen
        );
    }

    void onFixedProcess() {}
    void onTerminate() {}

    void respawn() {
        pos = Engine.randomCell();
        foreach (part; Engine.getSnake().body) {
            if (Vector2Equals(pos, part)) {
                respawn();
            }
        }
    }
}