graph [
  node [
    id 0
    label 1
    disk 2
    cpu 2
    memory 16
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 1
    memory 7
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 2
    memory 1
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 16
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 4
    memory 2
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 4
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 103
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 74
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 185
  ]
  edge [
    source 1
    target 3
    delay 31
    bw 177
  ]
  edge [
    source 1
    target 4
    delay 32
    bw 197
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 78
  ]
]
