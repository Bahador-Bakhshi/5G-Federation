graph [
  node [
    id 0
    label 1
    disk 7
    cpu 4
    memory 7
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 2
    memory 15
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 2
    memory 10
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 4
    memory 3
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 1
    memory 3
  ]
  node [
    id 5
    label 6
    disk 2
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
    delay 25
    bw 59
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 189
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 149
  ]
  edge [
    source 1
    target 3
    delay 27
    bw 108
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 104
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 98
  ]
]
