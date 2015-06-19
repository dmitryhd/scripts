#!/usr/bin/env lua

-- Prints all directories in given root directory.

package.path = package.path ..';/usr/share/lua/5.1/?'
package.cpath = package.cpath ..';/usr/local/lib/lua/5.1/?.so'


lfs = require"lfs"
--path = '/usr/share/lua/5.1/lfs.so'
--lfs = package.loadlib(path, "luaopen_socket")
root = '/home/dmitryhd/.config/awesome/themes/'


function isdir(fn)
    return (lfs.attributes(fn,"mode")== "directory")
end


-- Lua implementation of scandir function
function scandir(directory)
    local i, t, popen = 0, {}, io.popen
    for filename in popen('ls -a "'..directory..'"'):lines() do
        if isdir(root .. filename) then
            i = i + 1
            t[i] = filename
        end
    end
    return t
end


print(root)
dirs = scandir(root)
for k, v in pairs( dirs ) do
    print(k, v)
end
