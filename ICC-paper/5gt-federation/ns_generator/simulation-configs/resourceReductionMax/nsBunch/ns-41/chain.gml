graph [
  node [
    id 0
    label 1
    disk 1
    cpu 3
    memory 3
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 4
    memory 9
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 4
    memory 9
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 4
    memory 15
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 3
    memory 10
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 3
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 78
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 101
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 157
  ]
  edge [
    source 1
    target 3
    delay 25
    bw 108
  ]
  edge [
    source 2
    target 3
    delay 25
    bw 108
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 56
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 104
  ]
]
