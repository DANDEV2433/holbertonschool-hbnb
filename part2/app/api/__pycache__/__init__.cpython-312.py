�
    ko�g  �                   ��   � d dl mZ d dlmZ d dlmZ d dlmZ d dl	mZ
  eded��      Z eeddd	�
�      Zej                  ed��       ej                  ed��       ej                  e
d��       y)�    )�	Blueprint)�Api)�apir   z/api)�
url_prefixzMy APIz1.0z!API documentation for the project)�title�version�descriptionz
/amenities)�pathz/placesz/userN)�flaskr   �flask_restxr   �app.models.amenityr   �
amenity_ns�app.models.place�place_ns�app.models.user�user_ns�__name__�	blueprint�add_namespace� �    �4/root/holbertonschool-hbnb/part2/app/api/__init__.py�<module>r      ss   �� � � 0� ,� *��e�X�&�9�	�	��
��3�	�� � � �*�<� � 0� � � �(�� � +� � � �'�� � (r   