graph [
  node [
    id 0
    label 1
    disk 3
    cpu 3
    memory 10
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 1
    memory 10
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 3
    memory 9
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 2
    memory 14
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 4
    memory 4
  ]
  node [
    id 5
    label 6
    disk 5
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
    delay 27
    bw 136
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 113
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 129
  ]
  edge [
    source 0
    target 3
    delay 30
    bw 95
  ]
  edge [
    source 2
    target 4
    delay 26
    bw 187
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 125
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 144
  ]
]
