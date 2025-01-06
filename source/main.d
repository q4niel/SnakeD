import std.stdio;
import engine;

int main(string[] args) {
    if (!init()) {
        writeln("Error: Engine Initialization failed. Unable to set up the environment.");
    }

    while (runProc) {
        if (!proc()) {
            writeln("Error: Engine Processing failed. Encountered an unexpected issue during execution.");
        }
    }

    if (!term()) {
        writeln("Error: Engine Termination failed. Cleanup was not completed successfully.");
    }

    return 0;
}