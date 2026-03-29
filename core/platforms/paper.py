import os

class PaperGenerator:
    def generate(self, project):
        base = project.path

        # Создаём структуру папок
        src = os.path.join(base, "src", "main", "java", "mpm", project.name.lower())
        os.makedirs(src, exist_ok=True)

        # plugin.yml
        with open(os.path.join(base, "plugin.yml"), "w", encoding="utf-8") as f:
            f.write(f"name: {project.name}\n")
            f.write("version: 1.0\n")
            f.write("main: mpm." + project.name.lower() + ".Main\n")

        # Main.java
        with open(os.path.join(src, "Main.java"), "w", encoding="utf-8") as f:
            f.write("package mpm." + project.name.lower() + ";\n\n")
            f.write("import org.bukkit.plugin.java.JavaPlugin;\n\n")
            f.write("public class Main extends JavaPlugin {\n")
            f.write("    @Override\n")
            f.write("    public void onEnable() {\n")
            f.write("        getLogger().info(\"Plugin enabled!\");\n")
            f.write("    }\n")
            f.write("}\n")
