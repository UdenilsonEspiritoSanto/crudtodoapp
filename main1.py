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
            on_change=self.status_changed
        
        )
        self.edit_name = TextField(expand=1)#editar tarefa
        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_tasks,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(icon=icons.CREATE_OUTLINED, tooltip="Editar Tarefa",
                                   on_click=self.edit_clicked,
                                   icon_color=colors.GREEN,
                                   ),
                        IconButton(icon=icons.DELETE_OUTLINED, tooltip="Excluir Tarefa",
                                   on_click=self.delete_clicked,
                                   icon_color=colors.RED,
                                   ),
                                   
                    ],
                    
                ),
            ],

        )
        
    
        self.edit_view=Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Atualizar Tarefa",
                    on_click=self.save_clicked,
                )
            ]


        )
        return Column(controls=[self.display_view,self.display_tasks])
    
    def edit_clicked(self,e):
       self.edit_name.value = self.display_tasks.label
       self.display_view.visible = False
       self.edit_view.visible = True
       self.update()


    def delete_clicked(self,e):
      self.task_delete(self)

    def status_changed(self,e):
        self.completed = self.display_tasks.value
        self.task_status_change(self,e)

    def save_clicked(self,e):
       self.display_tasks.label = self.edit_name.value
       self.display_view.visible = True
       self.edit_view.visible = False
       self.update()

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
                        #input das tarefas
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
                                OutlinedButton(text="Limpar Tarefas Concluidas".upper(),
                                               on_click=self.clear_clicked,
                                               ),
                            ],

                        ),
                    ],

                ),
            ],
            
            )
        




    def add_clicked(self,e):
      if self.new_task.value:
          task=Task(self.new_task.value,self.tasks_status_change,self.task_delete)
          self.tasks.controls.append(task)
          self.new_task.value = ""
          self.new_task.focus()
          self.update()

    def tasks_status_change(self,task):
        pass
    def task_delete(self,task):
        pass
    
    def tabs_change():
        pass
    def clear_clicked():
        pass
    def update(self):
        status = self.filter.tabs[self.filter.selected.index].text
        cont = 0
        for task in self.tasks.controls:
            task.visible=(
                status =="Todas Tarefas"
                or (status == "Tarefas Ativas" and task.completed == False) 
                or (status == "Tarefas Completas" and task.completed == False)

            )
            if not task.completed:
                count+=1
            self.items_left.value = 'f{count}tarefa(s)adicionadas'    
            super().update()

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