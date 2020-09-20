graph [
  node [
    id 0
    label 1
    disk 2
    cpu 4
    memory 4
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 2
    memory 5
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 2
    memory 12
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 3
    memory 1
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 1
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 1
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 161
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 169
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 189
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 180
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 80
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 187
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 80
  ]
]
