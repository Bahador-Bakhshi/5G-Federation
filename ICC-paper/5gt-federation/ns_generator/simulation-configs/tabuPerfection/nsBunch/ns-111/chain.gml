graph [
  node [
    id 0
    label 1
    disk 3
    cpu 1
    memory 1
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 1
    memory 11
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 4
    memory 8
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 4
    memory 1
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 1
    memory 7
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 2
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 93
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 185
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 172
  ]
  edge [
    source 1
    target 3
    delay 29
    bw 157
  ]
  edge [
    source 2
    target 5
    delay 30
    bw 115
  ]
  edge [
    source 3
    target 4
    delay 28
    bw 64
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 140
  ]
]
