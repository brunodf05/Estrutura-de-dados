class Curso:
  turmas = []
  def __init__(self,nome):
    self.nome = nome
    self.t = Turma()
    
  def addTurma(self,turma):
    self.t = turma
    self.turmas.append(self.t)
    
  def removeTurma(self,nome):
    self.turmas.remove(nome)
    
  def printCurso(self):
    print(self.nome)
    print(turmas)
    
  def editCurso(self,nome):
    self.nome = nome
    
class Turma:
  blocos = []
  def __init__(self,nome):
    self.nome = nome
    self.b = Bloco()
    
  def addBloco(self,bloco):
    self.b = bloco
    self.turmas.append(self.b)
    
  def removeBloco(self,nome):
    self.turmas.remove(nome)
    
  def printTurma(self):
    print(self.nome)
    print(blocos)
    
  def editTurma(self,nome):
    self.nome = nome
    
class Bloco:
  disciplinas = []
  def __init__(self,nome):
    self.nome = nome
    self.d = Disciplinas()
    
  def addDisciplinas(self,disciplinas):
    self.d = disciplinas  
    self.turmas.append(self.d)
    
  def removeDisciplinas(self,nome):
    self.turmas.remove(nome)
    
  def printBlocos(self):
    print(self.nome)
    print(disciplinas)
    
  def editBloco(self,nome):
    self.nome = nome
    
class Disciplinas:
  def __init__(self,nome):
    self.nome = nome
    
  def editDisciplinas(self,nome):
    self.nome = nome
    

#para criacao dos objetos
nomecurso = input('Nome do Curso: ')
curso = Curso(nomecurso)

#para adição
nometurma = input('Nome da Turma para adicionar ao Curso: ')
turma = Turma(nometurma)
curso.addTurma(turma)

#para remocao
nometurma = input('Nome da Turma para remover de Curso: ')
curso.removeTurma(nometurma)

#para edição
nomecurso = input('Novo nome para curso: ')
curso.editCurso(nomecurso)

#para listar 
curso.printCurso()
