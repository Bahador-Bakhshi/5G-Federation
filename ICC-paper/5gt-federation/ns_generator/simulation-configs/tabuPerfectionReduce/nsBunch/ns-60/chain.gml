graph [
  node [
    id 0
    label 1
    disk 5
    cpu 2
    memory 5
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 2
    memory 12
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 2
    memory 2
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 4
    memory 12
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 1
    memory 8
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 4
    memory 3
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 122
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 98
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 114
  ]
  edge [
    source 0
    target 3
    delay 25
    bw 172
  ]
  edge [
    source 1
    target 5
    delay 31
    bw 98
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 68
  ]
  edge [
    source 3
    target 5
    delay 28
    bw 83
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 163
  ]
]
