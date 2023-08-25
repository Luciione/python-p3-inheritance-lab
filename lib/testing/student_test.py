#!/usr/bin/env python3

from teacher import Teacher
from user import User
        
class TestTeacher:
    '''Class "Teacher" in teacher.py'''

    


    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        my_teacher = Teacher("My", "Teacher")
        assert (my_teacher.first_name, my_teacher.last_name) == ("My", "Teacher")

    def test_initializes_with_knowledge(self):
        '''has an attribute called "knowledge", a list with len > 0.'''
        my_teacher = Teacher("My", "Teacher")
        assert hasattr(my_teacher, "knowledge")
        assert isinstance(my_teacher.knowledge, list)
        assert len(my_teacher.knowledge) > 0

    def test_can_teach(self):
        '''teaches from list of knowledge.'''
        my_teacher = Teacher("My", "Teacher")
        knowledge = ["Python basics", "Object-oriented programming"]
        my_teacher.knowledge = knowledge
        assert my_teacher.teach() in knowledge
