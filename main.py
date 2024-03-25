import flet
from flet import (
    Checkbox,
    Column,
    FloatingActionButton,
    IconButton,
    Page,
    Row,
    Tab,
    Tabs,
    TextField,
    UserControl,
    colors,
    icons,
)

class Task(UserControl):
         def __init__(self,task_name,task_delete):
                     super().__init__() 
                     self.task_name = task_name
                     self.task_delete = task_delete
         def build(self):
               self.display_task=Checkbox(value=False,label=self.task_name)
               self.edit_name = TextField(expand=1)

               self.display_view = Row(
                     alignment= "spaceBetween",
                     vertical_alignment="center",
                     controls=[
                           self.display_task,
                           Row(
                                 controls=[
                                       IconButton(icon=icons.CREATE_OUTLINED,
                                                     icon_color = "blue",
                                                     tooltip="Editar",
                                                     on_click=self.edit_clicked,
                                                     ),

                                                     IconButton(icon=icons.DELETE_OUTLINED,
                                                     icon_color = "red",
                                                     tooltip="Apagar",
                                                     on_click = self.delete_clicked,
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
                           self.edit_name,
                           IconButton(icon=icons.DONE_OUTLINE_OUTLINED,
                                         icon_color="green",
                                         tooltip="Salvar",
                                         on_click=self.save_clicked,
                                        
                                         )

                     ]
               )
               return Column(
                     controls=[self.display_view,self.edit_view]
               )
         def edit_clicked(self,e):
               self.edit_name.value=self.display_task.label
               self.display_view.visible = False
               self.edit_view.visible = True
               self.update()
         def save_clicked(self,e):
               self.display_task.label = self.edit_name.value
               self.display_view.visible = True
               self.edit_view.visible = False
               self.update()
         def delete_clicked(self,e):
               self.task_delete(self)

class TodoApp(UserControl):
          
        def build(self):
           self.tasks=[]
           self.new_task = TextField(hint_text="Digite aqui sua Tarefa",expand=True)
           self.tasks=Column()


           self.filter = Tabs(
                 selected_index=0,
                 on_change=self.tabs_changed,
                 tabs=[Tab(text="todos"),Tab(text="andamento"),Tab(text="Completadas")],
                                       ) 

           return Column(
           width=800,
           controls=[
            Row(
                controls=[
                    self.new_task,
                    FloatingActionButton(icon=icons.ADD,on_click=self.add_clicked)

                ],
            ),

           self.tasks,
        ],
    )    
        # FUNCAO DO BOTAO ADICIONAR()
        def add_clicked(self,e):
            task= Task(self.new_task.value,self.task_delete)
            self.tasks.controls.append(task)
            self.new_task.value=""
            self.update()

        def task_delete(self, task):
            self.tasks.controls.remove(task)
            self.update()   

        def update(self):
            status = self.filter.tabs[self.filter.selected_index].text
            for task in self.tasks.controls:
                task.visible = (
                status == "all"
                or (status == "active" and task.completed == False)
                or (status == "completed" and task.completed)
            )
            super().update()

        def tabs_changed(self, e):
          self.update()
     
      
        # FUNCAO PRINPAL MAIN
def main(page:Page):

    page.horizontal_alignment="center"
    page.update()
         
    todo=TodoApp()
    page.add(todo)
    


flet.app(target=main)