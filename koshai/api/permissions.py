# permissions.py

from rest_framework import permissions


class IsRestaurant(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_role("restaurant")


class IsCourier(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_role("courier")


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_role("customer")
