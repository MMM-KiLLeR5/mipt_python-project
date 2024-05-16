from PyQt5.QtWidgets import QAction


class MenuBar:
    @staticmethod
    def init_menu_bar(var):
        menubar = var.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")
        file.addAction(var.new_action)
        file.addAction(var.open_action)
        file.addAction(var.save_action)
        file.addAction(var.print_action)
        file.addAction(var.preview_action)
        edit.addAction(var.undo_action)
        edit.addAction(var.redo_action)
        edit.addAction(var.cut_action)
        edit.addAction(var.copy_action)
        edit.addAction(var.paste_action)

        edit.addAction(var.find_action)

        toolbar_action = QAction("Toggle Toolbar", var)
        toolbar_action.triggered.connect(lambda: MenuBar.toggle_toolbar(var))

        formatbar_action = QAction("Toggle Formatbar", var)
        formatbar_action.triggered.connect(lambda: MenuBar.toggle_formatbar(var))

        statusbar_action = QAction("Toggle Statusbar", var)
        statusbar_action.triggered.connect(lambda: MenuBar.toggle_statusbar(var))

        view.addAction(toolbar_action)
        view.addAction(formatbar_action)
        view.addAction(statusbar_action)

    @staticmethod
    def toggle_toolbar(var):
        state = var.toolbar.isVisible()

        var.toolbar.setVisible(not state)

    @staticmethod
    def toggle_formatbar(var):
        state = var.formatbar.isVisible()

        var.formatbar.setVisible(not state)

    @staticmethod
    def toggle_statusbar(var):
        state = var.statusbar.isVisible()

        var.statusbar.setVisible(not state)
