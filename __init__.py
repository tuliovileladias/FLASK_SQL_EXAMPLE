# -*- coding: UTF-8 -*-
import os
import sys
import json
import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime, timedelta
import urllib2
import time

#Congiguração do Flask e do Banco de Dados - Configure segundo a configuração do seu banco
#Os principais itens para alterar são: nome_usuario, senha, IP e nome_do_banco (schema)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://nome_usuario:senha@IP_DO_SEU_BANCO/nome_do_banco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
app.config['SQLALCHEMY_POOL_RECYCLE'] = 60
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
os.environ['TZ'] = 'America/Sao_Paulo'

# MODELO das Tabelas - Siga este mesmo padrão para linkar as tabelas cadastradas no seu banco
# Cada linha deve ser o nome da coluna que você deseja ter aqui.
class CadastroCliente(db.Model):
    __tablename__="cadastroCliente"
    idCliente = db.Column(db.Integer,primary_key=True)
    nomeCliente = db.Column(db.String(1000), nullable=False)
    cidadeCliente = db.Column(db.String(500),nullable=False)
    estadoCliente = db.Column(db.Integer)

#A função abaixo da rota, será executada sempre que for acionada esta rota
#Para acessar esta função, o link seria http://0.0.0.0:80/getCliente/22
#O que fica entre <> são variáveis que você pode passar para função
@app.route('/getCliente/<id_cliente>', methods=['GET']) 
def Infos_do_cliente(id_cliente):
    cliente = CadastroCliente.query.filter_by(idCliente=id_cliente).first()
    if(cliente is None):
        return "Nenhum cliente encontrado"
    else:
        return "{'name':'"+cliente.nomeCliente+"', 'cidade':'"+cliente.cidadeCliente+"'}"

def outros_exemplos():
    #Salvando um novo Dado
    cliente = CadastroCliente(nomeCliente="Joao", cidadeCliente="Santa Rita", estadoCliente="MG")
    db.session.add(cliente)
    #Alterando um Dado
    cliente = CadastroCliente.query.filter_by(idCliente=1).first()
    clinte.nome = "Novo Nome"
    db.session.commit()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80")