graph [
  node [
    id 0
    label 1
    disk 9
    cpu 3
    memory 3
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 3
    memory 14
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 3
    memory 13
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 2
    memory 6
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
    disk 2
    cpu 1
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
    bw 69
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 156
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 196
  ]
  edge [
    source 2
    target 3
    delay 35
    bw 80
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 160
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 124
  ]
]
