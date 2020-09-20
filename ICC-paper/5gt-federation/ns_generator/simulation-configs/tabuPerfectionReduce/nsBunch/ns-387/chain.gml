graph [
  node [
    id 0
    label 1
    disk 5
    cpu 4
    memory 3
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 1
    memory 15
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 4
    memory 2
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 2
    memory 11
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 1
    memory 14
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 3
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 78
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 94
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 64
  ]
  edge [
    source 1
    target 3
    delay 32
    bw 83
  ]
  edge [
    source 2
    target 4
    delay 30
    bw 116
  ]
  edge [
    source 3
    target 4
    delay 28
    bw 132
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 153
  ]
]
