import flet 

from flet import(

Page,
FloatingActionButton,
Column,
Checkbox,
IconButton,
OutlinedButton,
Tab,
Tabs,
Text,
TextField,
Row,
UserControl,
colors,
icons,
)#importacao dos componentes usados na aplicacao

#Classe de tarefas

class Task(UserControl):
    def __init__(self, task_name,task_status_change,task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete
   
    def build(self):
        self.display_tasks = Checkbox(
            value=False, label=self.task_name,
        
        )
        pass
#Classe Principal
class TodoApp(UserControl):
    def build(self):
        self.new_task=TextField(
            hint_text='digite aqui a nova tarefa',
            expand=True,
            on_submit=self.add_clicked,
            )
        self.tasks=Column()
        self.filter = Tabs(
           selected_index=0,
           on_change=self.tabs_change,
           tabs=[Tab(text = "Todas Tarefas"),Tab(text="Tarefas em Andamento"),Tab(text = "Tarefas Cocluidas"),],

        ),
        return Column(
            width=600,
            controls=[
                Row([Text(
                    value = "Tarefas", 
                    style = "headlineMedium",
                )],alignment="center"),
                Row(
                    controls=[
                        self.new_task,
                        
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                Column(
                    spacing=20,
                    controls=[
                        self.filter,
                        self.tasks,
                        Row(
                            alignment="spaceBetween",
                            vertical_alignment = "center",
                            controls=[
                                self.itens_left,
                                OutlinedButton(text="Limpar Tarefas Concuidas".upper(),
                                               on_click=self.clear_clicked,
                                               ),
                            ],

                        ),
                    ],

                ),
            ],
            
            )
        




    def add_clicked(self):
        pass    

    def tabs_change():
        pass


#funcao principal
def main(page:Page):
    page.title="Tarefas"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.update()


    #instancia da classe principal
    app = TodoApp()

    #adicionando a classe principal
    page.add(app)


flet.app(target=main)