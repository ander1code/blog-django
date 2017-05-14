from django.http import request
from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.models import User

# Authentication:
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import EmptyPage , Paginator , PageNotAnInteger
from datetime import datetime


def do_login(request):
    if request.method == 'POST':
        user = authenticate ( username=request.POST.get ( 'username' ) , password=request.POST.get ( 'password' ) )
        if user is not None:
            login ( request , user )
            messages.success ( request , 'Usuario logado com sucesso.' )
            return render ( request , 'home.html' )
        else:
            messages.error ( request , "Usuario e senha incorretos." )
    return render ( request , 'home.html' )


def home(request):
    posts = Postagem.objects.all ( ).order_by ( '-dataCriacao' )
    paginator = Paginator ( posts , 7 )
    page = request.GET.get ( 'page' )
    try:
        posts = paginator.page ( page )
    except PageNotAnInteger:
        posts = paginator.page ( 1 )
    except EmptyPage:
        posts = paginator.page ( paginator.num_pages )
    return render ( request , 'home.html' , {'posts': posts} )


@login_required ( login_url="/login/" )
def criar(request):
    if request.method == 'POST':
        frm = frmBlog ( request.POST , request.FILES )
        if frm.is_valid ( ):
            postagem = frm.save ( commit=False )
            postagem.autor_id = request.user.id
            postagem.titulo = frm.cleaned_data.get ( 'titulo' )
            postagem.texto = frm.cleaned_data.get ( 'texto' )
            postagem.imagem = frm.cleaned_data.get ( 'imagem' )
            postagem.dataCriacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            postagem.save ( )
            messages.success ( request , 'Postagem criada com sucesso.' )
            return render ( request , 'home.html')
        else:
            return render ( request , 'criacao.html' , {'form': frm} )
    else:
        dataCriacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        frm = frmBlog (
            initial={'autor': request.user.id , 'dataCriacao':dataCriacao, 'titulo': '' , 'texto': ''} )
    return render ( request , 'criacao.html' , {'form': frm , 'nome': request.user.username} )


def pesquisar(request):
    if request.POST:
        p_busca = request.POST['busca'] + '%'
        posts = Postagem.objects.extra ( where=["titulo LIKE %s"] , params=[p_busca] )
        if len ( posts ) == 0:
            messages.warning ( request , 'Nenhum artigo foi encontrado com esse criterio.' )
        paginator = Paginator ( posts , 7 )
        page = request.GET.get ( 'page' )
        try:
            posts = paginator.page ( page )
        except PageNotAnInteger:
            posts = paginator.page ( 1 )
        except EmptyPage:
            posts = paginator.page ( paginator.num_pages )
        return render ( request , 'pesquisa.html' , {'posts': posts} )
    return render ( request , "pesquisa.html" )


def show(request , id):
    post = get_object_or_404 ( Postagem , id=id )
    autor = User.objects.get ( id=post.autor_id )
    return render ( request , "show.html" , {'post': post , 'autor': autor} )


@login_required ( login_url='/login/' )
def editar(request , id):
    post = get_object_or_404 ( Postagem , id=id )
    if request.user.id == post.autor_id:
        if request.method == 'POST':
            frm = frmBlog ( request.POST , request.FILES , instance=post )
            if frm.is_valid ( ):
                postagem = frm.save ( commit=False )
                postagem.autor_id = request.user.id
                postagem.titulo = frm.cleaned_data.get ( 'titulo' )
                postagem.texto = frm.cleaned_data.get ( 'texto' )
                postagem.imagem = frm.cleaned_data.get ( 'imagem' )
                postagem.save ( )
                messages.success ( request , 'Postagem editada com sucesso.' )
                return render ( request , 'show.html' , {'post': postagem} )
            else:
                return render ( request , 'edicao.html' , {'form': frm , 'post_id': id} )
        else:
            frm = frmBlog ( initial={'autor': post.autor ,
                                     'titulo': post.titulo ,
                                     'texto': post.texto ,
                                     'imagem': post.imagem ,
                                     'dataCriacao': post.dataCriacao} )

        return render ( request , 'edicao.html' , {'form': frm , 'post_id': id} )
    else:
        messages.error ( request , 'Este usuario nao esta autorizado a editar esta postagem.' )
        return HttpResponseRedirect ( 'pesquisar' )


@login_required ( login_url='/login/' )
def excluir(request , id):
    post = get_object_or_404 ( Postagem , id=id )
    if request.user.id == post.autor_id:
        post.delete ( )
        messages.success ( request , 'Postagem excluida com sucesso.' )
        return HttpResponseRedirect ( 'pesquisar' )
    else:
        messages.error ( request , 'Este usuario nao esta autorizado a excluir esta postagem.' )
        return HttpResponseRedirect ( 'pesquisar' )
