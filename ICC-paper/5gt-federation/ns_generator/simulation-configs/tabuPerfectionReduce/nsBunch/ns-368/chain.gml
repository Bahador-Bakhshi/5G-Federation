graph [
  node [
    id 0
    label 1
    disk 4
    cpu 4
    memory 14
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 4
    memory 7
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 3
    memory 14
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 4
    memory 8
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 4
    memory 8
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 4
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 112
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 118
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 138
  ]
  edge [
    source 2
    target 3
    delay 35
    bw 99
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 177
  ]
  edge [
    source 2
    target 5
    delay 26
    bw 128
  ]
]
