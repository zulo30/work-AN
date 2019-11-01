## Copyright (C) 2019 Mateo Zuluaga Loaiza
## 
## This program is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see
## <https://www.gnu.org/licenses/>.

## -*- texinfo -*- 
## @deftypefn {} {@var{retval} =} splineNatural (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Mateo Zuluaga Loaiza <zulo30@MacBook-Pro-de-Mateo-Zuluaga-Loaiza.local>
## Created: 2019-10-31

function S = splineNatural  (X, Y)


## Se inicializan las variables auxiliares 
n = length(X)
a = Y(1:n);


## Paso 1
for i=1:n-1
    h(i) = X(i+1) - X(i);
endfor

## Paso 2
for i=2:n-1
    alfa(1,i) = (3/h(1,i)) * (Y(i+1)- Y(i)) - (3/h(1,i-1)) * (Y(i)- Y(i-1));
endfor

## Paso 3
ele(1,1) = 1;
mu(1,1) = 0;
z(1,1) = 0;


## Paso 4
for i=2:n-1
    ele(1,i) =  2*(X(i+1) - X(i-1))- h(1,i-1) * mu(1,i-1);
    mu(1,i) = h(1,i)/ele(1,i);
    z(1,i) = (alfa(1,i)-h(1,i-1)*z(1,i-1))/ele(1,i);
endfor

ele
mu
z

## Paso 5
ele(n) = 1;
mu(n) = 0;
c(n) = 0;

## Paso 6
k = n-1;
while (k > 0 )
    c(k) = z(k) - (mu(1,k)* c(k+1));
    b(k) = (Y(k+1) - Y(k))/h(1,k) -  h(1,k)*(c(k+1) + 2*c(k))/3;
    d(k) = (c(k+1) - c(k))/(3*h(1,k));
    k--;
endwhile
c
b 
d

## Paso 7   Salida (aj,bj,cj,dj para j = 0,1, ... , n-1);
S = armarMatrixSolucion(X,Y,b,c,d);
## Pare.

endfunction


##  
##  Esta funcion es para armar la matriz solucion
## 

function S = armarMatrixSolucion(x,y,b,c,d)
    n = length(x);
    S = []; ## se inicializa la variable de la matriz S
    for i=1:n-1
        S(i,1) = i;
        S(i,2) = x(1,i);
        S(i,3) = y(1,i);
        S(i,4) = b(1,i);
        S(i,5) = c(1,i);
        S(i,6) = d(1,i);
    endfor
    S(n,1) = n;
    S(n,2) = x(1,n);
    S(n,3) = y(1,n);
    
endfunction 