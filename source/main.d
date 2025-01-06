import std.stdio;
import engine;

int main(string[] args) {
    if (!Engine.initialize()) {
        writeln("Error: Engine Initialization failed. Unable to set up the environment.");
    }

    while (Engine.shouldProcess) {
        if (!Engine.process()) {
            writeln("Error: Engine Processing failed. Encountered an unexpected issue during execution.");
        }
    }

    if (!Engine.terminate()) {
        writeln("Error: Engine Termination failed. Cleanup was not completed successfully.");
    }

    return 0;
}