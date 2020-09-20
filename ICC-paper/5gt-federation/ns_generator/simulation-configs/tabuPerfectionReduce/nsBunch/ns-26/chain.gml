graph [
  node [
    id 0
    label 1
    disk 5
    cpu 1
    memory 12
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 4
    memory 12
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 1
    memory 5
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 2
    memory 9
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 3
    memory 8
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 3
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 189
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 99
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 78
  ]
  edge [
    source 1
    target 3
    delay 25
    bw 74
  ]
  edge [
    source 2
    target 3
    delay 30
    bw 54
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 169
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 111
  ]
]
