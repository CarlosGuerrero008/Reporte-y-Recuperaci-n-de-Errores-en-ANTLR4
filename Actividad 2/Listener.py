from SimpleListener import SimpleListener

class ClaseMetodoAsignacionListener(SimpleListener):
    def enterClassDef(self, ctx):
        class_name = ctx.ID().getText()
        print(f"Clase: {class_name}")

    def enterMember(self, ctx):
        if ctx.getChildCount() > 2 and ctx.getChild(2).getText() == '(':
            method_name = ctx.ID(0).getText()
            print(f"Método: {method_name}")

    def enterStat(self, ctx):
        if ctx.getChildCount() >= 3 and ctx.getChild(1).getText() == '=':
            var_name = ctx.getChild(0).getText()
            print(f"Asignación: {var_name} = ...")
