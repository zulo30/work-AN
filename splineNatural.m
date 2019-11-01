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

function [a,b,c,d] = splineNatural  (X, Y)


## Se inicializan las variables auxiliares 

n = length(X)- 1

a = Y(1:n)

b = zeros(1,n);
c = zeros(1,n);
d = zeros(1,n);

h = zeros(1,n);


alfa = zeros(1,n);
ele = zeros(1,n);
mu = zeros(1,n);
z = zeros(1,n);



## Paso 1
for i=1:n
    h(1,i) = X(i+1) - X(i);
endfor
h
## Paso 2
for i=2:n-1
    alfa(1,i) = (3/h(1,i)) * (Y(i+1)- Y(i)) - (3/h(1,i-1)) * (Y(i)- Y(i-1))
endfor

## Paso 3
ele(1) = 1;
mu(1) = 0;
z(1) = 0;

## Paso 4
for i=2:n-1
    l(1,i) =  2*(X(i+1) - X(i-1))- h(1,i-1) * mu(1,i-1);
    mu(1,i) = h(1,i)/ele(1,i);

    z(1,i) = (alfa(1,i)-h(1,i-1)*z(1,i-1))/ele(1,i);
endfor

## Paso 5
ele(n) = 1;
mu(n) = 0;
c(n) = 0;

## Paso 6
key = n - 1;
while (key > 0 )
    c(1,key) = z(1,key) - (mu(1,key)* c(1,key+1));
    b(1,key) = (Y(key+1) - Y(key))/h(1,key) -  h(1,key)*(c(1,key+1) + 2*c(1,key))/3;
    d(1,key) = (c(1,key+1) - c(1,key))/(3*h(1,key));
    key--
endwhile

## Paso 7   Salida (aj,bj,cj,dj para j = 0,1, ... , n-1);
## Pare.

endfunction
