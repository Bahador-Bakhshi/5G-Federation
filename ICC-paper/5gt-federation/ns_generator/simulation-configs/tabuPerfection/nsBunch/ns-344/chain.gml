graph [
  node [
    id 0
    label 1
    disk 4
    cpu 4
    memory 13
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 1
    memory 10
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 1
    memory 9
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 2
    memory 8
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 1
    memory 9
  ]
  node [
    id 5
    label 6
    disk 3
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
    delay 33
    bw 56
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 166
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 69
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 61
  ]
  edge [
    source 1
    target 4
    delay 25
    bw 67
  ]
  edge [
    source 2
    target 4
    delay 34
    bw 187
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 188
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 98
  ]
]
