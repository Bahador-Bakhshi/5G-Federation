graph [
  node [
    id 0
    label 1
    disk 7
    cpu 4
    memory 6
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 1
    memory 1
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 3
    memory 13
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 1
    memory 15
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 3
    memory 4
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 4
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 125
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 150
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 148
  ]
  edge [
    source 2
    target 3
    delay 33
    bw 73
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 169
  ]
  edge [
    source 3
    target 5
    delay 28
    bw 122
  ]
]
