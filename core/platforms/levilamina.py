import os

class LeviLaminaGenerator:
    def generate(self, project):
        base = project.path

        # CMakeLists.txt
        with open(os.path.join(base, "CMakeLists.txt"), "w", encoding="utf-8") as f:
            f.write("cmake_minimum_required(VERSION 3.20)\n")
            f.write(f"project({project.name})\n")
            f.write("add_library(plugin SHARED main.cpp)\n")

        # main.cpp
        with open(os.path.join(base, "main.cpp"), "w", encoding="utf-8") as f:
            f.write("#include <ll/api/plugin/Plugin.h>\n\n")
            f.write("class PluginMain : public ll::Plugin {\n")
            f.write("public:\n")
            f.write("    bool load() override { return true; }\n")
            f.write("    bool enable() override { return true; }\n")
            f.write("    bool disable() override { return true; }\n")
            f.write("};\n\n")
            f.write("LL_REGISTER_PLUGIN(PluginMain);\n")
