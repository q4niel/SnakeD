import std.stdio;
import engine;

int main(string[] args) {
    if (!Engine.on()) {
        writeln("Error: Engine Initialization failed. Unable to set up the environment.");
    }

    while (Engine.runnable) {
        if (!Engine.run()) {
            writeln("Error: Engine Processing failed. Encountered an unexpected issue during execution.");
        }
    }

    if (!Engine.off()) {
        writeln("Error: Engine Termination failed. Cleanup was not completed successfully.");
    }

    return 0;
}