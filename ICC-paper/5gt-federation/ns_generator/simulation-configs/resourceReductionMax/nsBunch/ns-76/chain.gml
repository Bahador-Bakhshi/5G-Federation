graph [
  node [
    id 0
    label 1
    disk 7
    cpu 2
    memory 15
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 3
    memory 9
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 2
    memory 13
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 3
    memory 4
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 3
    memory 4
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 3
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 134
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 114
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 54
  ]
  edge [
    source 1
    target 3
    delay 31
    bw 105
  ]
  edge [
    source 2
    target 3
    delay 26
    bw 168
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 194
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 169
  ]
]
