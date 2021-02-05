graph [
  node [
    id 0
    label 1
    disk 6
    cpu 2
    memory 14
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 4
    memory 13
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 1
    memory 9
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 1
    memory 16
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 2
    memory 7
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 2
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 175
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 144
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 71
  ]
  edge [
    source 0
    target 3
    delay 30
    bw 98
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 112
  ]
  edge [
    source 2
    target 4
    delay 34
    bw 121
  ]
  edge [
    source 3
    target 4
    delay 32
    bw 91
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 106
  ]
]
