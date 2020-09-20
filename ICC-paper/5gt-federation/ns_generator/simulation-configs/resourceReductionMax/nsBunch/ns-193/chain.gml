graph [
  node [
    id 0
    label 1
    disk 6
    cpu 1
    memory 5
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 2
    memory 6
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 1
    memory 6
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 4
    memory 10
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 2
    memory 10
  ]
  node [
    id 5
    label 6
    disk 10
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
    delay 29
    bw 173
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 144
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 61
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 179
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 100
  ]
  edge [
    source 2
    target 4
    delay 34
    bw 146
  ]
  edge [
    source 3
    target 4
    delay 32
    bw 53
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 116
  ]
]
