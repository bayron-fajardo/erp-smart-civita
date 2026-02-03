from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GroupForm, PermissionForm



#@login_required
def lista_roles(request):
    roles = Group.objects.all()
    return render(request, 'roles_permisos/roles/lista.html', {'roles': roles})


#@login_required
def crear_rol(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rol creado exitosamente')
            return redirect('lista_roles')
    else:
        form = GroupForm()
    return render(request, 'roles_permisos/roles/crear.html', {'form': form})


#@login_required
def editar_rol(request, rol_id):
    rol = get_object_or_404(Group, id=rol_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rol actualizado exitosamente')
            return redirect('lista_roles')
    else:
        form = GroupForm(instance=rol)
    return render(request, 'roles_permisos/roles/editar.html', {'form': form, 'rol': rol})


#login_required
def eliminar_rol(request, rol_id):
    rol = get_object_or_404(Group, id=rol_id)
    if request.method == 'POST':
        rol.delete()
        messages.success(request, 'Rol eliminado exitosamente')
        return redirect('lista_roles')
    return render(request, 'roles_permisos/roles/eliminar.html', {'rol': rol})


#@login_required
def lista_permisos(request):
    permisos = Permission.objects.all()
    return render(request, 'roles_permisos/permisos/lista.html', {'permisos': permisos})


@login_required
def crear_permiso(request):
    if request.method == 'POST':
        form = PermissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Permiso creado exitosamente')
            return redirect('lista_permisos')
    else:
        form = PermissionForm()
    return render(request, 'roles_permisos/permisos/crear.html', {'form': form})


@login_required
def editar_permiso(request, permiso_id):
    permiso = get_object_or_404(Permission, id=permiso_id)
    if request.method == 'POST':
        form = PermissionForm(request.POST, instance=permiso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Permiso actualizado exitosamente')
            return redirect('lista_permisos')
    else:
        form = PermissionForm(instance=permiso)
    return render(request, 'roles_permisos/permisos/editar.html', {'form': form, 'permiso': permiso})


@login_required
def eliminar_permiso(request, permiso_id):
    permiso = get_object_or_404(Permission, id=permiso_id)
    if request.method == 'POST':
        permiso.delete()
        messages.success(request, 'Permiso eliminado exitosamente')
        return redirect('lista_permisos')
    return render(request, 'roles_permisos/permisos/eliminar.html', {'permiso': permiso})

@login_required
def eliminar_rol(request, rol_id):
    rol = get_object_or_404(Group, id=rol_id)
    if request.method == 'POST':
        rol.delete()
        messages.success(request, 'Rol eliminado exitosamente')
        return redirect('lista_roles')
    return render(request, 'roles_permisos/roles/eliminar.html', {'rol': rol})


@login_required
def eliminar_permiso(request, permiso_id):
    permiso = get_object_or_404(Permission, id=permiso_id)
    if request.method == 'POST':
        permiso.delete()
        messages.success(request, 'Permiso eliminado exitosamente')
        return redirect('lista_permisos')
    return render(request, 'roles_permisos/permisos/eliminar.html', {'permiso': permiso})
