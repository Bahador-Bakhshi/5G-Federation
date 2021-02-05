graph [
  node [
    id 0
    label 1
    disk 1
    cpu 1
    memory 16
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 1
    memory 16
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 4
    memory 5
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 4
    memory 2
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 3
    memory 4
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 2
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 66
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 124
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 197
  ]
  edge [
    source 1
    target 3
    delay 27
    bw 99
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 64
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 54
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 149
  ]
]
